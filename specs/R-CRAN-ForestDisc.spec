%global packname  ForestDisc
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Forest Discretization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-stats 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-moments 
Requires:         R-stats 

%description
Supervised, multivariate, and non-parametric discretization algorithm
based on tree ensembles learning and moment matching optimization. This
version of the algorithm relies on random forest algorithm to learn a
large set of split points that conserves the relationship between
attributes and the target class, and on moment matching optimization to
transform this set into a reduced number of cut points matching as well as
possible statistical properties of the initial set of split points. For
each attribute to be discretized, the set S of its related split points
extracted through random forest is mapped to a reduced set C of cut points
of size k. This mapping relies on minimizing, for each continuous
attribute to be discretized, the distance between the four first moments
of S and the four first moments of C subject to some constraints. This
non-linear optimization problem is performed using k values ranging from 2
to 'max_splits', and the best solution returned correspond to the value k
which optimum solution is the lowest one over the different realizations.
ForestDisc is a generalization of RFDisc discretization method initially
proposed by Berrado and Runger (2009) <doi:10.1109/AICCSA.2009.5069327>,
and improved by Berrado et al. in 2012 by adopting the idea of moment
matching optimization related by Hoyland and Wallace (2001) <doi:
10.1287/mnsc.47.2.295.9834>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
