%global packname  veccompare
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Perform Set Operations on Vectors, Automatically Generating Alln-Wise Comparisons, and Create Markdown Output

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-VennDiagram 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-gtools 
Requires:         R-grid 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-VennDiagram 

%description
Automates set operations (i.e., comparisons of overlap) between multiple
vectors. It also contains a function for automating reporting in
'RMarkdown', by generating markdown output for easy analysis, as well as
an 'RMarkdown' template for use with 'RStudio'.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
