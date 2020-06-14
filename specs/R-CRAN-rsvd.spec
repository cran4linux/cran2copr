%global packname  rsvd
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          2%{?dist}
Summary:          Randomized Singular Value Decomposition

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-Matrix 
Requires:         R-Matrix 

%description
Low-rank matrix decompositions are fundamental tools and widely used for
data analysis, dimension reduction, and data compression. Classically,
highly accurate deterministic matrix algorithms are used for this task.
However, the emergence of large-scale data has severely challenged our
computational ability to analyze big data. The concept of randomness has
been demonstrated as an effective strategy to quickly produce approximate
answers to familiar problems such as the singular value decomposition
(SVD). The rsvd package provides several randomized matrix algorithms such
as the randomized singular value decomposition (rsvd), randomized
principal component analysis (rpca), randomized robust principal component
analysis (rrpca), randomized interpolative decomposition (rid), and the
randomized CUR decomposition (rcur). In addition several plot functions
are provided.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
