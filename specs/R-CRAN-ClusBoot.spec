%global __brp_check_rpaths %{nil}
%global packname  ClusBoot
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Bootstrap Clustering

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Clustering algorithms are designed to cluster objects into a number of
clusters. Any clustering algorithm provides the 'best' grouping of objects
according to some criterion. This does not guarantee a 'good' clustering
solution in the sense that some allocations were not simply the result of
chance. This package allows the user to apply any clustering algorithm to
a data set. The cluster allocations are subjected to a bootstrap analysis
to determine the extent to which the clustering structure is stable and
fundamental to the data set. For more information see
<https://slubbe.wixsite.com/academic-cv/conference-presentations>.

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
