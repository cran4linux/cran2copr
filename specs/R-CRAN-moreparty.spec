%global packname  moreparty
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          A Toolbox for Conditional Inference Random Forests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-varImp 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-measures 
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-iml 
BuildRequires:    R-CRAN-pdp 
BuildRequires:    R-CRAN-vip 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-party 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-varImp 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-measures 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-iml 
Requires:         R-CRAN-pdp 
Requires:         R-CRAN-vip 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 

%description
Additions to 'party' package : tools for the interpretation of forests
(surrogate trees, prototypes, etc.), feature selection (see Gregorutti et
al (2017) <arXiv:1310.5726>, Hapfelmeier and Ulm (2013)
<doi:10.1016/j.csda.2012.09.020>, Altmann et al (2010)
<doi:10.1093/bioinformatics/btq134>) and parallelized versions of
conditional forest and variable importance functions.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
