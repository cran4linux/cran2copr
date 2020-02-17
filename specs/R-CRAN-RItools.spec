%global packname  RItools
%global packver   0.1-17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.17
Release:          1%{?dist}
Summary:          Randomization Inference Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-svd 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-survival 
Requires:         R-CRAN-SparseM 
Requires:         R-grDevices 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-svd 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-survival 

%description
Tools for randomization-based inference. Current focus is on the d^2
omnibus test of differences of means following Hansen and Bowers (2008)
useful for assessing balance in matched observational studies or for
analysis of outcomes in block-randomized experiments.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
