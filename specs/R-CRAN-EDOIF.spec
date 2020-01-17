%global packname  EDOIF
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Empirical Distribution Ordering Inference Framework (EDOIF)

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-distr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-simpleboot 
Requires:         R-CRAN-ggplot2 >= 3.0
Requires:         R-boot 
Requires:         R-CRAN-distr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-simpleboot 

%description
A non-parametric framework based on estimation statistics principle. Its
main purpose is to infer orders of empirical distributions from different
categories based on a probability of finding a value in one distribution
that is greater than an expectation of another distribution. Given a set
of ordered-pair of real-category values the framework is capable of 1)
inferring orders of domination of categories and representing orders in
the form of a graph; 2) estimating magnitude of difference between a pair
of categories in forms of mean-difference confidence intervals; and 3)
visualizing domination orders and magnitudes of difference of categories.
The publication of this package is at Chainarong Amornbunchornvej,
Navaporn Surasvadi, Anon Plangprasopchok, and Suttipong Thajchayapong
(2019) <arXiv:1911.06723>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/EDOIF_0.1.1.pdf
%{rlibdir}/%{packname}/INDEX
