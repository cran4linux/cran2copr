%global debug_package %{nil}
%global packname  GGMM
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Mixture Gaussian Graphical Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-equSA 
BuildRequires:    R-CRAN-huge 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-equSA 
Requires:         R-CRAN-huge 

%description
The Gaussian graphical model is a widely used tool for learning gene
regulatory networks with high-dimensional gene expression data. For many
real problems, the data are heterogeneous, which may contain some
subgroups or come from different resources. This package provide a
Gaussian Graphical Mixture Model (GGMM) for the heterogeneous data. You
can refer to Jia, B. and Liang, F. (2018) at <arXiv:1805.02547> for
detail.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
