%global packname  TechPhD
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Tests and Estimation of Covariance Change-Points for Hi-Dim Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 

%description
An implementation of the procedures in Zhong et al. (2019) and Santo and
Zhong (2020) for testing the homogeneity of covariance matrices, and
estimating multiple change-points in high-dimensional (Hi-Dim)
longitudinal/functional data with general temporospatial dependence. The
null hypothesis of the homogeneity test is that all covariance matrices
are equal at each time point. If the null hypothesis is rejected, the
procedure further identifies the locations of the change points. Note: The
package uses Open MP.  Mac OS X users may need to update clang compiler so
that it supports Open MP. References: Ping-Shou Zhong, Runze Li, Shawn
Santo (2019) <doi:10.1093/biomet/asz011> Shawn Santo, Ping-Shou Zhong
(2020) <arXiv:2005.01895>.

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
%{rlibdir}/%{packname}/libs
