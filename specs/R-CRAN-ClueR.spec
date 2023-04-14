%global __brp_check_rpaths %{nil}
%global packname  ClueR
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Cluster Evaluation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-parallel 
Requires:         R-CRAN-e1071 
Requires:         R-parallel 

%description
CLUster Evaluation (CLUE) is a computational method for identifying
optimal number of clusters in a given time-course dataset clustered by
cmeans or kmeans algorithms and subsequently identify key kinases or
pathways from each cluster. Its implementation in R is called ClueR. See
README on <https://github.com/PengyiYang/ClueR> for more details. P Yang
et al. (2015) <doi:10.1371/journal.pcbi.1004403>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
