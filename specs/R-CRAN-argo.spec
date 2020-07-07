%global packname  argo
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          3%{?dist}
Summary:          Accurate Estimation of Influenza Epidemics using Google SearchData

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-Matrix 
BuildRequires:    R-boot 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-xtable 
Requires:         R-Matrix 
Requires:         R-boot 

%description
Augmented Regression with General Online data (ARGO) for accurate
estimation of influenza epidemics in United States on both national level
and regional level. It replicates the method introduced in paper Yang, S.,
Santillana, M. and Kou, S.C. (2015) <doi:10.1073/pnas.1515373112> and
Ning, S., Yang, S. and Kou, S.C. (2019) <doi:10.1038/s41598-019-41559-6>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/regiondata
%{rlibdir}/%{packname}/INDEX
