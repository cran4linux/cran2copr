%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  imprinting
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Birth Year-Specific Probabilities of Immune Imprinting to Influenza

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-cowplot >= 1.0.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-cowplot >= 1.0.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyselect 

%description
Reconstruct birth-year specific probabilities of immune imprinting to
influenza A, using the methods of Gostic et al. (2016)
<doi:10.1126/science.aag1322>. Plot, save, or export the calculated
probabilities for use in your own research. By default, the package
calculates subtype-specific imprinting probabilities, but with
user-provided frequency data, it is possible to calculate probabilities
for arbitrary kinds of primary exposure to influenza A, including primary
vaccination and exposure to specific clades, strains, etc.

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
