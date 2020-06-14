%global packname  binGroup
%global packver   2.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          2%{?dist}
Summary:          Evaluation and Experimental Design for Binomial Group Testing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-partitions 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-utils 

%description
Methods for estimation and hypothesis testing of proportions in group
testing designs: methods for estimating a proportion in a single
population (assuming sensitivity and specificity equal to 1 in designs
with equal group sizes), as well as hypothesis tests and functions for
experimental design for this situation. For estimating one proportion or
the difference of proportions, a number of confidence interval methods are
included, which can deal with various different pool sizes. Further,
regression methods are implemented for simple pooling and matrix pooling
designs. Methods for identification of positive items in group testing
designs: Optimal testing configurations can be found for hierarchical and
array-based algorithms. Operating characteristics can be calculated for
testing configurations across a wide variety of situations.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
