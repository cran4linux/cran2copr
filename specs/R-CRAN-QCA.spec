%global packname  QCA
%global packver   3.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.11
Release:          1%{?dist}%{?buildtag}
Summary:          Qualitative Comparative Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-admisc >= 0.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-venn 
Requires:         R-CRAN-admisc >= 0.10
Requires:         R-methods 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-venn 

%description
An extensive set of functions to perform Qualitative Comparative Analysis:
crisp sets ('csQCA'), temporal ('tQCA'), multi-value ('mvQCA') and fuzzy
sets ('fsQCA'), using a GUI - graphical user interface. 'QCA' is a
methodology that bridges the qualitative and quantitative divide in social
science research. It uses a Boolean algorithm, resulting in a minimal
causal configuration that explains a given phenomenon.

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
