%global packname  productivity
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Indices of Productivity Using Data Envelopment Analysis (DEA)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.3
Requires:         R-core >= 2.15.3
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-methods 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-methods 

%description
Levels and changes of productivity and profitability are measured with
various indices. The package contains the multiplicatively complete
Färe-Primont, Fisher, Hicks-Moorsteen, Laspeyres, Lowe, and Paasche
indices, as well as the classic Malmquist productivity index. Färe-Primont
and Lowe indices verify the transitivity property and can therefore be
used for multilateral or multitemporal comparison. Fisher,
Hicks-Moorsteen, Laspeyres, Malmquist, and Paasche indices are not
transitive and are only to be used for binary comparison. All indices can
also be decomposed into different components, providing insightful
information on the sources of productivity and profitability changes. In
the use of Malmquist productivity index, the technological change index
can be further decomposed into bias technological change components. The
package also allows to prohibit technological regression (negative
technological change). In the case of the Fisher, Hicks-Moorsteen,
Laspeyres, Paasche and the transitive Färe-Primont and Lowe indices, it is
furthermore possible to rule out technological change. Deflated shadow
prices can also be obtained. Besides, the package allows parallel
computing as an option, depending on the user's computer configuration.
All computations are carried out with the nonparametric Data Envelopment
Analysis (DEA), and several assumptions regarding returns to scale are
available. All DEA linear programs are implemented using 'lp_solve'.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
