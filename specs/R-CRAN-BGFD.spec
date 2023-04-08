%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BGFD
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bell-G and Complementary Bell-G Family of Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-AdequacyModel 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-AdequacyModel 
Requires:         R-graphics 
Requires:         R-stats 

%description
Evaluates the probability density function, cumulative distribution
function, quantile function, random numbers, survival function, hazard
rate function, and maximum likelihood estimates for the following
distributions: Bell exponential, Bell extended exponential, Bell Weibull,
Bell extended Weibull, Bell-Fisk, Bell-Lomax, Bell Burr-XII, Bell Burr-X,
complementary Bell exponential, complementary Bell extended exponential,
complementary Bell Weibull, complementary Bell extended Weibull,
complementary Bell-Fisk, complementary Bell-Lomax, complementary Bell
Burr-XII and complementary Bell Burr-X distribution. Related work
includes: a) Fayomi A., Tahir M. H., Algarni A., Imran M. and Jamal F.
(2022). "A new useful exponential model with applications to quality
control and actuarial data". Computational Intelligence and Neuroscience,
2022. <doi:10.1155/2022/2489998>. b) Alanzi, A. R., Imran M., Tahir M. H.,
Chesneau C., Jamal F. Shakoor S. and Sami, W. (2023). "Simulation
analysis, properties and applications on a new Burr XII model based on the
Bell-X functionalities". AIMS Mathematics, 8(3): 6970-7004.
<doi:10.3934/math.2023352>. c) Algarni A. (2022). "Group Acceptance
Sampling Plan Based on New Compounded Three-Parameter Weibull Model".
Axioms, 11(9): 438. <doi:10.3390/axioms11090438>.

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
