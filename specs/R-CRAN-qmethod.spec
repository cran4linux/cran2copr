%global __brp_check_rpaths %{nil}
%global packname  qmethod
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Subjective Perspectives Using Q Methodology

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rjson 
Requires:         R-methods 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-GPArotation 
Requires:         R-tools 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rjson 

%description
Analysis of Q methodology, used to identify distinct perspectives existing
within a group. This methodology is used across social, health and
environmental sciences to understand diversity of attitudes, discourses,
or decision-making styles (for more information, see
<https://qmethod.org/>). A single function runs the full analysis. Each
step can be run separately using the corresponding functions: for
automatic flagging of Q-sorts (manual flagging is optional), for statement
scores, for distinguishing and consensus statements, and for general
characteristics of the factors. The package allows to choose either
principal components or centroid factor extraction, manual or automatic
flagging, a number of mathematical methods for rotation (or none), and a
number of correlation coefficients for the initial correlation matrix,
among many other options. Additional functions are available to import and
export data (from raw *.CSV, 'HTMLQ' and 'FlashQ' *.CSV, 'PQMethod' *.DAT
and 'easy-htmlq' *.JSON files), to print and plot, to import raw data from
individual *.CSV files, and to make printable cards. The package also
offers functions to print Q cards and to generate Q distributions for
study administration. See further details in the package documentation,
and in the web pages below, which include a cookbook, guidelines for more
advanced analysis (how to perform manual flagging or change the sign of
factors), data management, and a beta graphical user interface for online
and offline use.

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
