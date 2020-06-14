%global packname  irtDemo
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          2%{?dist}
Summary:          Item Response Theory Demo Collection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildArch:        noarch
BuildRequires:    R-CRAN-fGarch >= 3010.82
BuildRequires:    R-CRAN-shiny >= 0.13.2
Requires:         R-CRAN-fGarch >= 3010.82
Requires:         R-CRAN-shiny >= 0.13.2

%description
Includes a collection of shiny applications to demonstrate or to explore
fundamental item response theory (IRT) concepts such as estimation,
scoring, and multidimensional IRT models.

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
%doc %{rlibdir}/%{packname}/DICH
%doc %{rlibdir}/%{packname}/EAPMAP
%doc %{rlibdir}/%{packname}/EST2PL
%doc %{rlibdir}/%{packname}/EST3PL
%doc %{rlibdir}/%{packname}/GPCM
%doc %{rlibdir}/%{packname}/GRM
%doc %{rlibdir}/%{packname}/GRSM
%doc %{rlibdir}/%{packname}/MIRT
%doc %{rlibdir}/%{packname}/MLE
%doc %{rlibdir}/%{packname}/NRM
%{rlibdir}/%{packname}/INDEX
