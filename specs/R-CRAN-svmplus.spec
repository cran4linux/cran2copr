%global __brp_check_rpaths %{nil}
%global packname  svmplus
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Implementation of Support Vector Machines Plus (SVM+)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
Requires:         R-CRAN-quadprog 
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-MASS 

%description
Implementation of Support Vector Machines Plus (SVM+) for classification
problems. See (Vladimir et. al, 2009, <doi:10.1016/j.neunet.2009.06.042>)
for theoretical details and see (Li et. al, 2016,
<https://github.com/okbalefthanded/svmplus_matlab>) for implementation
details in 'MATLAB'.

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
