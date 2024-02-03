%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  REffectivePred
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pandemic Prediction Model in an SIRS Framework

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-config 
Requires:         R-CRAN-zoo 
Requires:         R-grDevices 
Requires:         R-utils 

%description
A suite of methods to fit and predict case count data using a
compartmental SIRS (Susceptible – Infectious – Recovered – Susceptible)
model, based on an assumed specification of the effective reproduction
number. The significance of this approach is that it relates epidemic
progression to the average number of contacts of infected individuals,
which decays as a function of the total susceptible fraction remaining in
the population. The main functions are pred.curve(), which computes the
epidemic curve for a set of parameters, and estimate.mle(), which finds
the best fitting curve to observed data. The easiest way to pass arguments
to the functions is via a config file, which contains input settings
required for prediction, and the package offers two methods,
navigate_to_config() which points the user to the configuration file, and
re_predict() for starting the fit-predict process. Razvan G. Romanescu et
al. (2023) <doi:10.1016/j.epidem.2023.100708>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
