%global __brp_check_rpaths %{nil}
%global packname  MSGARCHelm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hybridization of MS-GARCH and ELM Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-nnfor 
BuildRequires:    R-CRAN-MSGARCH 
BuildRequires:    R-CRAN-forecast 
Requires:         R-CRAN-nnfor 
Requires:         R-CRAN-MSGARCH 
Requires:         R-CRAN-forecast 

%description
Implements the three parallel forecast combinations of Markov Switching
GARCH and extreme learning machine model along with the selection of
appropriate model for volatility forecasting. For method details see Hsiao
C, Wan SK (2014). <doi:10.1016/j.jeconom.2013.11.003>, Hansen BE (2007).
<doi:10.1111/j.1468-0262.2007.00785.x>, Elliott G, Gargano A, Timmermann A
(2013). <doi:10.1016/j.jeconom.2013.04.017>.

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
