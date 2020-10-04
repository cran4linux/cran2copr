%global packname  tstools
%global packver   0.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.8
Release:          3%{?dist}%{?buildtag}
Summary:          A Time Series Toolbox for Official Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.7.12
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-zoo >= 1.7.12
Requires:         R-CRAN-xts 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-data.table 

%description
Plot official statistics' time series conveniently: automatic legends,
highlight windows, stacked bar chars with positive and negative
contributions, sum-as-line option, two y-axes with automatic horizontal
grids that fit both axes and other popular chart types. 'tstools' comes
with a plethora of defaults to let you plot without setting an abundance
of parameters first, but gives you the flexibility to tweak the defaults.
In addition to charts, 'tstools' provides a super fast, 'data.table'
backed time series I/O that allows the user to export / import long
format, wide format and transposed wide format data to various file types.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/example_data
%doc %{rlibdir}/%{packname}/marc_vja_examples.R
%doc %{rlibdir}/%{packname}/vja.xlsx
%{rlibdir}/%{packname}/INDEX
