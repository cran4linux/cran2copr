%global packname  CA3variants
%global packver   2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5
Release:          3%{?dist}
Summary:          Three-Way Correspondence Analysis Variants

License:          GPL (> 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel > 3.0.1
Requires:         R-core > 3.0.1
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-multichull 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-multichull 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 

%description
Provides four variants of three-way correspondence analysis (ca):
three-way symmetrical ca, three-way non-symmetrical ca, three-way ordered
symmetrical ca and three-way ordered non-symmetrical ca.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
