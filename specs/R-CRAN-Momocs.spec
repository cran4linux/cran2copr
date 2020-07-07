%global packname  Momocs
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          3%{?dist}
Summary:          Morphometrics using R

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-geomorph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegan 
Requires:         R-cluster 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-geomorph 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-jpeg 
Requires:         R-MASS 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-sp 
Requires:         R-utils 
Requires:         R-CRAN-vegan 

%description
The development of this package is now over, it is superseded by Momocs2
and more generally MomX ecosystem. The goal of Momocs is to provide a
complete, convenient, reproducible and open-source toolkit for 2D
morphometrics. It includes most common 2D morphometrics approaches on
outlines, open outlines, configurations of landmarks, traditional
morphometrics, and facilities for data preparation, manipulation and
visualization with a consistent grammar throughout. It allows
reproducible, complex morphometrics analyses and other morphometrics
approaches should be easy to plug in, or develop from, on top of this
canvas.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
