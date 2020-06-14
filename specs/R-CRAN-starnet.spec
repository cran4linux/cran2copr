%global packname  starnet
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          2%{?dist}
Summary:          Stacked Elastic Net

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-cornet 
BuildRequires:    R-CRAN-joinet 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-glmnet 
Requires:         R-survival 
Requires:         R-CRAN-cornet 
Requires:         R-CRAN-joinet 
Requires:         R-Matrix 

%description
Implements stacked elastic net regression (Rauschenberger 2020,
<doi:10.1093/bioinformatics/btaa535>). The elastic net generalises ridge
and lasso regularisation (Zou 2005,
<doi:10.1111/j.1467-9868.2005.00503.x>). Instead of fixing or tuning the
mixing parameter alpha, we combine multiple alpha by stacked
generalisation (Wolpert 1992 <doi:10.1016/S0893-6080(05)80023-1>).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
