%global packname  metapro
%global packver   1.5.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.8
Release:          1%{?dist}
Summary:          Robust P-Value Combination Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-metap 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rSymPy 
Requires:         R-CRAN-metap 
Requires:         R-stats 
Requires:         R-CRAN-rSymPy 

%description
The meta-analysis is performed to increase the statistical power by
integrating the results from several experiments. The p-values are often
combined in meta-analysis when the effect sizes are not available. The
'metapro' R package provides not only traditional methods (Becker BJ
(1994, ISBN:0-87154-226-9), Mosteller, F. & Bush, R.R. (1954,
ISBN:0201048523) and Lancaster HO (1949, ISSN:00063444)), but also new
methods such as weighted Fisher’s method and ordmeta we developed. While
the (weighted) Z-method is suitable for finding features effective in most
experiments, (weighted) Fisher’s method and ordmeta are useful for
detecting partially associated features. Thus, the users can choose the
function based on their purpose.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
