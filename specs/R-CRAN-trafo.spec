%global packname  trafo
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Estimation, Comparison and Selection of Transformations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lmtest 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-pryr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lmtest 

%description
Estimation, selection and comparison of several families of
transformations. The families of transformations included in the package
are the following: Bickel-Doksum (Bickel and Doksum 1981
<doi:10.2307/2287831>), Box-Cox, Dual (Yang 2006
<doi:10.1016/j.econlet.2006.01.011>), Glog (Durbin et al. 2002
<doi:10.1093/bioinformatics/18.suppl_1.S105>), gpower (Kelmansky et al.
2013 <doi:10.1515/sagmb-2012-0030>), Log, Log-shift opt (Feng et al. 2016
<doi:10.1002/sta4.104>), Manly, modulus (John and Draper 1980
<doi:10.2307/2986305>), Neglog (Whittaker et al. 2005
<doi:10.1111/j.1467-9876.2005.00520.x>), Reciprocal and Yeo-Johnson. The
package simplifies to compare linear models with untransformed and
transformed dependent variable as well as linear models where the
dependent variable is transformed with different transformations.
Furthermore, the package employs maximum likelihood approaches, moments
optimization and divergence minimization to estimate the optimal
transformation parameter.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
