%global packname  clusterability
%global packver   0.1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1.0
Release:          3%{?dist}
Summary:          Performs Tests for Cluster Tendency of a Data Set

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-diptest 
BuildRequires:    R-splines 
Requires:         R-CRAN-diptest 
Requires:         R-splines 

%description
Test for cluster tendency (clusterability) of a data set. The methods
implemented - reducing the data set to a single dimension using principal
component analysis or computing pairwise distances, and performing a
multimodality test like the Dip Test or Silverman's Critical Bandwidth
Test - are described in Adolfsson, Ackerman, and Brownstein (2019)
<doi:10.1016/j.patcog.2018.10.026>. Such methods can inform whether
clustering algorithms are appropriate for a data set.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
