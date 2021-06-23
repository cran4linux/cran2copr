%global __brp_check_rpaths %{nil}
%global packname  MTAR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Multi-Trait Analysis of Rare-Variant Association Study

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.51.4
BuildRequires:    R-CRAN-CompQuadForm >= 1.4.3
BuildRequires:    R-Matrix >= 1.2.2
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-MASS >= 7.3.51.4
Requires:         R-CRAN-CompQuadForm >= 1.4.3
Requires:         R-Matrix >= 1.2.2
Requires:         R-stats 
Requires:         R-utils 

%description
Perform multi-trait rare-variant association tests using the summary
statistics and adjust for possible sample overlap. Package is based on
"Multi-Trait Analysis of Rare-Variant Association Summary Statistics using
MTAR" by Luo, L., Shen, J., Zhang, H., Chhibber, A. Mehrotra, D.V., Tang,
Z., 2019 (submitted).

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
