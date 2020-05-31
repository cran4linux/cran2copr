%global packname  RKEELjars
%global packver   1.0.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.19
Release:          1%{?dist}
Summary:          Java Executable .jar Files for 'RKEEL'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-downloader 
BuildRequires:    R-utils 
Requires:         R-CRAN-downloader 
Requires:         R-utils 

%description
'KEEL' is a popular Java software for a large number of different
knowledge data discovery tasks. Furthermore, 'RKEEL' is a package with a R
code layer between R and 'KEEL', for using 'KEEL' in R code. This package
downloads and install the .jar files necessary for 'RKEEL' algorithms
execution. For more information about 'KEEL', see <http://www.keel.es/>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/exe
%{rlibdir}/%{packname}/INDEX
