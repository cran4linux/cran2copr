%global packname  ppclust
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Probabilistic and Possibilistic Cluster Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-inaparc 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-inaparc 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
Partitioning clustering divides the objects in a data set into
non-overlapping subsets or clusters by using the prototype-based
probabilistic and possibilistic clustering algorithms. This package covers
a set of the functions for Fuzzy C-Means (Bezdek, 1974)
<doi:10.1080/01969727308546047>, Possibilistic C-Means (Krishnapuram &
Keller, 1993) <doi:10.1109/91.227387>, Possibilistic Fuzzy C-Means (Pal et
al, 2005) <doi:10.1109/TFUZZ.2004.840099>, Possibilistic Clustering
Algorithm (Yang et al, 2006) <doi:10.1016/j.patcog.2005.07.005>,
Possibilistic C-Means with Repulsion (Wachs et al, 2006)
<doi:10.1007/3-540-31662-0_6> and the other variants of hard and soft
clustering algorithms. The cluster prototypes and membership matrices
required by these partitioning algorithms are initialized with different
initialization techniques that are available in the package 'inaparc'. As
the distance metrics, not only the Euclidean distance but also a set of
the commonly used distance metrics are available to use with some of the
algorithms in the package.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
