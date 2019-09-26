%global packname  ttTensor
%global packver   0.99.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.2
Release:          1%{?dist}
Summary:          Tensor-Train Decomposition

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-CRAN-tensorr 
BuildRequires:    R-CRAN-PTAk 
BuildRequires:    R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-rTensor 
Requires:         R-CRAN-tensorr 
Requires:         R-CRAN-PTAk 
Requires:         R-Matrix 

%description
Tensor-train is a compact representation for higher-order tensors. Some
algorithms for performing tensor-train decomposition are available such as
TT-SVD, TT-WOPT, and TT-Cross. For the details of the algorithms, see I.
V. Oseledets (2011) <doi:10.1137/090752286>, Yuan Longao, et al (2017)
<arXiv:1709.02641>, I. V. Oseledets (2010)
<doi:10.1016/j.laa.2009.07.024>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
