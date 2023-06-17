%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  corx
%global packver   1.0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Create and Format Correlation Matrices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ppcor 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-ppcor 

%description
Create correlation (or partial correlation) matrices. Correlation matrices
are formatted with significance stars based on user preferences. Matrices
of coefficients, p-values, and number of pairwise observations are
returned. Send resultant formatted matrices to the clipboard to be pasted
into excel and other programs. A plot method allows users to visualize
correlation matrices created with 'corx'.

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
