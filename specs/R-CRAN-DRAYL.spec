%global packname  DRAYL
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Computation of Rayleigh Densities of Arbitrary Dimension

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-RConics 
BuildRequires:    R-CRAN-rmutil 
BuildRequires:    R-CRAN-cubature 
Requires:         R-stats 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-RConics 
Requires:         R-CRAN-rmutil 
Requires:         R-CRAN-cubature 

%description
We offer an implementation of the series representation put forth in "A
series representation for multidimensional Rayleigh distributions" by
Wiegand and Nadarajah <DOI: 10.1002/dac.3510>. Furthermore we have
implemented an integration approach proposed by Beaulieu et al. for 3 and
4-dimensional Rayleigh densities (Beaulieu, Zhang, "New simplest exact
forms for the 3D and 4D multivariate Rayleigh PDFs with applications to
antenna array geometrics", <DOI: 10.1109/TCOMM.2017.2709307>).

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
