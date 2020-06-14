%global packname  TopicScore
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          2%{?dist}
Summary:          The Topic SCORE Algorithm to Fit Topic Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-slam 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-quadprog 
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-CRAN-slam 

%description
Provides implementation of the "Topic SCORE" algorithm that is proposed by
Tracy Ke and Minzhe Wang. The singular value decomposition step is
optimized through the usage of svds() function in 'RSpectra' package, on a
'dgRMatrix' sparse matrix. Also provides a column-wise error measure in
the word-topic matrix A, and an algorithm for recovering the
topic-document matrix W given A and D based on quadratic programming. The
details about the techniques are explained in the paper "A new SVD
approach to optimal topic estimation" by Tracy Ke and Minzhe Wang (2017)
<arXiv:1704.07016>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
