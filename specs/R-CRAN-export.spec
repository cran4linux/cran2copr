%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  export
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Streamlined Export of Graphs and Data Tables

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stargazer >= 5.2.1
BuildRequires:    R-CRAN-openxlsx >= 4.0.17
BuildRequires:    R-CRAN-devEMF >= 3.8
BuildRequires:    R-CRAN-xtable >= 1.8.2
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-broom >= 0.4.4
BuildRequires:    R-CRAN-flextable >= 0.4.3
BuildRequires:    R-CRAN-officer >= 0.2.2
BuildRequires:    R-CRAN-rvg >= 0.1.8
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-datasets 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-stargazer >= 5.2.1
Requires:         R-CRAN-openxlsx >= 4.0.17
Requires:         R-CRAN-devEMF >= 3.8
Requires:         R-CRAN-xtable >= 1.8.2
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-broom >= 0.4.4
Requires:         R-CRAN-flextable >= 0.4.3
Requires:         R-CRAN-officer >= 0.2.2
Requires:         R-CRAN-rvg >= 0.1.8
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-datasets 
Requires:         R-grDevices 

%description
Easily export 'R' graphs and statistical output to 'Microsoft Office' /
'LibreOffice', 'Latex' and 'HTML' Documents, using sensible defaults that
result in publication-quality output with simple, straightforward
commands. Output to 'Microsoft Office' is in editable 'DrawingML' vector
format for graphs, and can use corporate template documents for styling.
This enables the production of standardized reports and also allows for
manual tidy-up of the layout of 'R' graphs in 'Powerpoint' before final
publication. Export of graphs is flexible, and functions enable the
currently showing R graph or the currently showing 'R' stats object to be
exported, but also allow the graphical or tabular output to be passed as
objects. The package relies on package 'officer' for export to 'Office'
documents,and output files are also fully compatible with 'LibreOffice'.
Base 'R', 'ggplot2' and 'lattice' plots are supported, as well as a wide
variety of 'R' stats objects, via wrappers to xtable(), broom::tidy() and
stargazer(), including aov(), lm(), glm(), lme(), glmnet() and coxph() as
well as matrices and data frames and many more...

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
