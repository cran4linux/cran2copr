%global packname  mdsOpt
%global packver   0.4-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          3%{?dist}
Summary:          Searching for Optimal MDS Procedure for Metric andInterval-Valued Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-smacof 
BuildRequires:    R-CRAN-clusterSim 
BuildRequires:    R-CRAN-symbolicDA 
BuildRequires:    R-CRAN-smds 
BuildRequires:    R-CRAN-animation 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-spdep 
Requires:         R-CRAN-smacof 
Requires:         R-CRAN-clusterSim 
Requires:         R-CRAN-symbolicDA 
Requires:         R-CRAN-smds 
Requires:         R-CRAN-animation 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-spdep 

%description
Selecting the optimal multidimensional scaling (MDS) procedure for metric
data via metric MDS (ratio, interval, mspline) and nonmetric MDS
(ordinal). Selecting the optimal multidimensional scaling (MDS) procedure
for interval-valued data via metric MDS (ratio, interval,
mspline).Selecting the optimal multidimensional scaling procedure for
interval-valued data by varying all combinations of normalization and
optimization methods.Selecting the optimal MDS procedure for statistical
data referring to the evaluation of tourist attractiveness of Lower
Silesian counties. (Borg, I., Groenen, P.J.F., Mair, P. (2013)
<doi:10.1007/978-3-642-31848-1>, Groenen, P.J.F., Winsberg, S., Rodriguez,
O., Diday, E. (2006) <doi:10.1016/j.csda.2006.04.003>, Walesiak, M. (2016)
<doi:10.15611/ekt.2016.2.01>, Walesiak, M. (2017)
<doi:10.15611/ekt.2017.3.01>).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
