%global __brp_check_rpaths %{nil}
%global packname  rankFD
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rank-Based Tests for General Factorial Designs

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.43
BuildRequires:    R-CRAN-coin >= 1.1.2
BuildRequires:    R-CRAN-lattice >= 0.20.33
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-MASS >= 7.3.43
Requires:         R-CRAN-coin >= 1.1.2
Requires:         R-CRAN-lattice >= 0.20.33
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-mvtnorm 

%description
The rankFD() function calculates the Wald-type statistic (WTS) and the
ANOVA-type statistic (ATS) for nonparametric factorial designs, e.g., for
count, ordinal or score data in a crossed design with an arbitrary number
of factors. Brunner, E., Bathke, A. and Konietschke, F. (2018)
<doi:10.1007/978-3-030-02914-2>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
