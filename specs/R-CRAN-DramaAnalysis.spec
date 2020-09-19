%global packname  DramaAnalysis
%global packver   3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Dramatic Texts

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-git2r >= 0.24.0
BuildRequires:    R-CRAN-tokenizers >= 0.2.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-git2r >= 0.24.0
Requires:         R-CRAN-tokenizers >= 0.2.1
Requires:         R-stats 
Requires:         R-utils 

%description
Analysis of preprocessed dramatic texts, with respect to literary
research. The package provides functions to analyze and visualize
information about characters, stage directions, the dramatic structure and
the text itself. The dramatic texts are expected to be in CSV format,
which can be installed from within the package, sample texts are provided.
The package and the reasoning behind it are described in Reiter et al.
(2017) <doi:10.18420/in2017_119>.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
