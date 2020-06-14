%global packname  MTSYS
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          2%{?dist}
Summary:          Methods in Mahalanobis-Taguchi (MT) System

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Mahalanobis-Taguchi (MT) system is a collection of multivariate analysis
methods developed for the field of quality engineering. MT system consists
of two families depending on their purpose. One is a family of
Mahalanobis-Taguchi (MT) methods (in the broad sense) for diagnosis (see
Woodall, W. H., Koudelik, R., Tsui, K. L., Kim, S. B., Stoumbos, Z. G.,
and Carvounis, C. P. (2003) <doi:10.1198/004017002188618626>) and the
other is a family of Taguchi (T) methods for forecasting (see Kawada, H.,
and Nagata, Y. (2015) <doi:10.17929/tqs.1.12>). The MT package contains
three basic methods for the family of MT methods and one basic method for
the family of T methods. The MT method (in the narrow sense), the
Mahalanobis-Taguchi Adjoint (MTA) methods, and the Recognition-Taguchi
(RT) method are for the MT method and the two-sided Taguchi (T1) method is
for the family of T methods. In addition, the Ta and Tb methods, which are
the improved versions of the T1 method, are included.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
