%global packname  FSA
%global packver   0.8.30
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.30
Release:          3%{?dist}
Summary:          Simple Fisheries Stock Assessment Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dunn.test 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-sciplot 
BuildRequires:    R-CRAN-withr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-car 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dunn.test 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-sciplot 
Requires:         R-CRAN-withr 

%description
A variety of simple fish stock assessment methods. Detailed vignettes are
available on the fishR website <http://derekogle.com/fishR/>.

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
%doc %{rlibdir}/%{packname}/helpers
%{rlibdir}/%{packname}/INDEX
