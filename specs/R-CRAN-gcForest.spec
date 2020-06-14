%global packname  gcForest
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          2%{?dist}
Summary:          Deep Forest Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-pkgdown 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-utils 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-pkgdown 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 
Requires:         R-utils 

%description
R application programming interface (API) for Deep Forest which based on
Zhou and Feng (2017). Deep Forest: Towards an Alternative to Deep Neural
Networks. (<arXiv:1702.08835v2>) or Zhou and Feng (2017). Deep Forest.
(<arXiv:1702.08835>). And for the Python module 'gcForest'
(<https://github.com/pylablanche/gcForest>).

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/python
%{rlibdir}/%{packname}/INDEX
