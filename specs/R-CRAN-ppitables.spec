%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ppitables
%global packver   0.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.5
Release:          1%{?dist}%{?buildtag}
Summary:          Lookup Tables to Generate Poverty Likelihoods and Rates using the Poverty Probability Index (PPI)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
The Poverty Probability Index (PPI) is a poverty measurement tool for
organizations and businesses with a mission to serve the poor. The PPI is
statistically-sound, yet simple to use: the answers to 10 questions about
a household’s characteristics and asset ownership are scored to compute
the likelihood that the household is living below the poverty line – or
above by only a narrow margin. This package contains country-specific
lookup data tables used as reference to determine the poverty likelihood
of a household based on their score from the country-specific PPI
questionnaire. These lookup tables have been extracted from documentation
of the PPI found at <https://www.povertyindex.org> and managed by
Innovations for Poverty Action <https://poverty-action.org/>.

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
