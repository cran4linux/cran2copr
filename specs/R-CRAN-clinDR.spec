%global packname  clinDR
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          1%{?dist}
Summary:          Simulation and Analysis Tools for Clinical Dose ResponseModeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rstan >= 2.17.3
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DoseFinding 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-rstan >= 2.17.3
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DoseFinding 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
Bayesian and ML Emax model fitting, graphics and simulation for clinical
dose response.  The summary data from the dose response meta-analyses in
Thomas, Sweeney, and Somayaji (2014) <doi:10.1080/19466315.2014.924876>
and Thomas and Roy (2016) <doi:10.1080/19466315.2016.1256229> Wu,
Banerjee, Jin, Menon, Martin, and Heatherington(2017)
<doi:10.1177/0962280216684528> are included in the package.  The prior
distributions for the Bayesian analyses default to the posterior
predictive distributions derived from these references.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
