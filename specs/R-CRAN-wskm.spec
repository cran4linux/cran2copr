%global packname  wskm
%global packver   1.4.40
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.40
Release:          2%{?dist}
Summary:          Weighted k-Means Clustering

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-fpc 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-fpc 

%description
Entropy weighted k-means (ewkm) by Liping Jing, Michael K. Ng and Joshua
Zhexue Huang (2007) <doi:10.1109/TKDE.2007.1048> is a weighted subspace
clustering algorithm that is well suited to very high dimensional data.
Weights are calculated as the importance of a variable with regard to
cluster membership.  The two-level variable weighting clustering algorithm
tw-k-means (twkm) by Xiaojun Chen, Xiaofei Xu, Joshua Zhexue Huang and
Yunming Ye (2013) <doi:10.1109/TKDE.2011.262> introduces two types of
weights, the weights on individual variables and the weights on variable
groups, and they are calculated during the clustering process.  The
feature group weighted k-means (fgkm) by Xiaojun Chen, Yunminng Ye,
Xiaofei Xu and Joshua Zhexue Huang (2012)
<doi:10.1016/j.patcog.2011.06.004> extends this concept by grouping
features and weighting the group in addition to weighting individual
features.

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
