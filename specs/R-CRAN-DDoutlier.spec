%global packname  DDoutlier
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Distance & Density-Based Outlier Detection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-pracma 

%description
Outlier detection in multidimensional domains. Implementation of notable
distance and density-based outlier algorithms. Allows users to identify
local outliers by comparing observations to their nearest neighbors,
reverse nearest neighbors, shared neighbors or natural neighbors. For
distance-based approaches, see Knorr, M., & Ng, R. T. (1997)
<doi:10.1145/782010.782021>, Angiulli, F., & Pizzuti, C. (2002)
<doi:10.1007/3-540-45681-3_2>, Hautamaki, V., & Ismo, K. (2004)
<doi:10.1109/ICPR.2004.1334558> and Zhang, K., Hutter, M. & Jin, H. (2009)
<doi:10.1007/978-3-642-01307-2_84>. For density-based approaches, see
Tang, J., Chen, Z., Fu, A. W. C., & Cheung, D. W. (2002)
<doi:10.1007/3-540-47887-6_53>, Jin, W., Tung, A. K. H., Han, J., & Wang,
W. (2006) <doi:10.1007/11731139_68>, Schubert, E., Zimek, A. & Kriegel,
H-P. (2014) <doi:10.1137/1.9781611973440.63>, Latecki, L., Lazarevic, A. &
Prokrajac, D. (2007) <doi:10.1007/978-3-540-73499-4_6>, Papadimitriou, S.,
Gibbons, P. B., & Faloutsos, C. (2003) <doi:10.1109/ICDE.2003.1260802>,
Breunig, M. M., Kriegel, H.-P., Ng, R. T., & Sander, J. (2000)
<doi:10.1145/342009.335388>, Kriegel, H.-P., Kröger, P., Schubert, E., &
Zimek, A. (2009) <doi:10.1145/1645953.1646195>, Zhu, Q., Feng, Ji. &
Huang, J. (2016) <doi:10.1016/j.patrec.2016.05.007>, Huang, J., Zhu, Q.,
Yang, L. & Feng, J. (2015) <doi:10.1016/j.knosys.2015.10.014>, Tang, B. &
Haibo, He. (2017) <doi:10.1016/j.neucom.2017.02.039> and Gao, J., Hu, W.,
Zhang, X. & Wu, Ou. (2011) <doi:10.1007/978-3-642-20847-8_23>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
