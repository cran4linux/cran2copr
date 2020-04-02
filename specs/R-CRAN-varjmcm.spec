%global packname  varjmcm
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Estimations for the Covariance of Estimated Parameters in JointMean-Covariance Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jmcm 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-jmcm 
Requires:         R-CRAN-expm 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-Matrix 

%description
The goal of the package is to equip the 'jmcm' package (current version
0.2.1) with estimations of the covariance of estimated parameters. Two
methods are provided. The first method is to use the inverse of estimated
Fisher's information matrix, see M. Pourahmadi (2000)
<doi:10.1093/biomet/87.2.425>, M. Maadooliat, M. Pourahmadi and J. Z.
Huang (2013) <doi:10.1007/s11222-011-9284-6>, and W. Zhang, C. Leng, C.
Tang (2015) <doi:10.1111/rssb.12065>. The second method is bootstrap
based, see Liu, R.Y. (1988) <doi:10.1214/aos/1176351062> for reference.

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
%{rlibdir}/%{packname}/INDEX
