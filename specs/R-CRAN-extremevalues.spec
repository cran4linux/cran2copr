%global __brp_check_rpaths %{nil}
%global packname  extremevalues
%global packver   2.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.3
Release:          3%{?dist}%{?buildtag}
Summary:          Univariate Outlier Detection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8.0
Requires:         R-core >= 2.8.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gWidgets2 
BuildRequires:    R-CRAN-gWidgets2tcltk 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-gWidgets2 
Requires:         R-CRAN-gWidgets2tcltk 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 

%description
Detect outliers in one-dimensional data.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
