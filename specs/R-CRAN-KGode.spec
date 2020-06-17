%global packname  KGode
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Kernel Based Gradient Matching for Parameter Inference inOrdinary Differential Equations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-pspline 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-pspline 
Requires:         R-CRAN-mvtnorm 

%description
The kernel ridge regression and the gradient matching algorithm proposed
in Niu et al. (2016) <http://jmlr.org/proceedings/papers/v48/niu16.html>
and the warping algorithm proposed in Niu et al. (2017)
<DOI:10.1007/s00180-017-0753-z> are implemented for parameter inference in
differential equations. Four schemes are provided for improving parameter
estimation in odes by using the odes regularisation and warping.

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
%{rlibdir}/%{packname}/INDEX
