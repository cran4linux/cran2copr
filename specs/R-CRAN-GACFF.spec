%global __brp_check_rpaths %{nil}
%global packname  GACFF
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Genetic Similarity in User-Based Collaborative Filtering

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
The genetic algorithm can be used directly to find the similarity of users
and more effectively to increase the efficiency of the collaborative
filtering method. By identifying the nearest neighbors to the active user,
before the genetic algorithm, and by identifying suitable starting points,
an effective method for user-based collaborative filtering method has been
developed. This package uses an optimization algorithm (continuous genetic
algorithm) to directly find the optimal similarities between active users
(users for whom current recommendations are made) and others. First, by
determining the nearest neighbor and their number, the number of genes in
a chromosome is determined. Each gene represents the neighbor's similarity
to the active user. By estimating the starting points of the genetic
algorithm, it quickly converges to the optimal solutions. The positive
point is the independence of the genetic algorithm on the number of data
that for big data is an effective help in solving the problem.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
