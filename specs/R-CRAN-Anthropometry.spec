%global packname  Anthropometry
%global packver   1.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.14
Release:          2%{?dist}
Summary:          Statistical Methods for Anthropometric Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-shapes 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-archetypes 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-depth 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-ICGE 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-biclust 
Requires:         R-CRAN-shapes 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-archetypes 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-depth 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-ICGE 
Requires:         R-cluster 
Requires:         R-CRAN-biclust 

%description
Statistical methodologies especially developed to analyze anthropometric
data. These methods are aimed at providing effective solutions to some
commons problems related to Ergonomics and Anthropometry. They are based
on clustering, the statistical concept of data depth, statistical shape
analysis and archetypal analysis. Please see Vinue (2017)
<doi:10.18637/jss.v077.i06>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
