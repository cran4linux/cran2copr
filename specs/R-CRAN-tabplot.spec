%global packname  tabplot
%global packver   1.3-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          1%{?dist}
Summary:          Tableplot, a Visualization of Large Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ffbase >= 0.12.3
BuildRequires:    R-CRAN-bit 
BuildRequires:    R-CRAN-ff 
BuildRequires:    R-grid 
Requires:         R-CRAN-ffbase >= 0.12.3
Requires:         R-CRAN-bit 
Requires:         R-CRAN-ff 
Requires:         R-grid 

%description
A tableplot is a visualisation of a (large) dataset with a dozen of
variables, both numeric and categorical. Each column represents a variable
and each row bin is an aggregate of a certain number of records. Numeric
variables are visualized as bar charts, and categorical variables as
stacked bar charts. Missing values are taken into account. Also supports
large 'ffdf' datasets from the 'ff' package.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
