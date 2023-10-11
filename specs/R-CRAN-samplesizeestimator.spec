%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  samplesizeestimator
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Sample Size for Various Scenarios

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-stats 

%description
Calculates sample size for various scenarios, such as sample size to
estimate population proportion with stated absolute or relative precision,
testing a single proportion with a reference value, to estimate the
population mean with stated absolute or relative precision, testing single
mean with a reference value and sample size for comparing two unpaired or
independent means, comparing two paired means, the sample size For case
control studies, estimating the odds ratio with stated precision, testing
the odds ratio with a reference value, estimating relative risk with
stated precision, testing relative risk with a reference value, testing a
correlation coefficient with a specified value, etc.
<https://www.academia.edu/39511442/Adequacy_of_Sample_Size_in_Health_Studies#:~:text=Determining%%20the%%20sample%%20size%%20for,may%%20yield%%20statistically%%20inconclusive%%20results.>.

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
