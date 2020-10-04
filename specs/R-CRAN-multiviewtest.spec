%global packname  multiviewtest
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Hypothesis Tests for Association Between Subgroups in Two DataViews

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-randnet 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-randnet 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 

%description
Tests for association between subgroups in two multivariate data views,
two network data views, or a multivariate data view and a network data
view. (Reference 1 is Gao, L.L., Bien, J., and Witten, D. (2019) Are
Clusterings of Multiple Data Views Independent? to appear in
Biostatistics, Reference 2 is Gao, L.L., Witten, D., Bien, J. Testing for
Association in Multi-View Network Data, preprint.)

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
%{rlibdir}/%{packname}/INDEX
