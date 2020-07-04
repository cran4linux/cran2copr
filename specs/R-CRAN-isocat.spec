%global packname  isocat
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}
Summary:          Isotope Origin Clustering and Assignment Tools

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-foreach 
Requires:         R-utils 
Requires:         R-CRAN-raster 
Requires:         R-stats 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-foreach 

%description
This resource provides tools to create, compare, and post-process spatial
isotope assignment models of animal origin. It generates
probability-of-origin maps for individuals based on user-provided tissue
and environment isotope values (e.g., as generated by IsoMAP, Bowen et al.
[2013] <doi:10.1111/2041-210X.12147>) using the framework established in
Bowen et al. (2010) <doi:10.1146/annurev-earth-040809-152429>). The
package 'isocat' can then quantitatively compare and cluster these maps to
group individuals by similar origin. It also includes techniques for
applying four approaches (cumulative sum, odds ratio, quantile only, and
quantile simulation) with which users can summarize geographic origins and
probable distance traveled by individuals. Campbell et al. [2020]
establishes several of the functions included in this package
<doi:10.1515/ami-2020-0004>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
