%global packname  piRF
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Prediction Intervals for Random Forests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-Rdpack 

%description
Implements multiple state-of-the-art prediction interval methodologies for
random forests. These include: quantile regression intervals, out-of-bag
intervals, bag-of-observations intervals, one-step boosted random forest
intervals, bias-corrected intervals, high-density intervals, and
split-conformal intervals. The implementations include a combination of
novel adjustments to the original random forest methodology and novel
prediction interval methodologies. All of these methodologies can be
utilized using solely this package, rather than a collection of separate
packages. Currently, only regression trees are supported. Also capable of
handling high dimensional data. Roy, Marie-Helene and Larocque, Denis
(2019) <doi:10.1177/0962280219829885>. Ghosal, Indrayudh and Hooker, Giles
(2018) <arXiv:1803.08000>. Zhu, Lin and Lu, Jiaxin and Chen, Yihong (2019)
<arXiv:1905.10101>. Zhang, Haozhe and Zimmerman, Joshua and Nettleton, Dan
and Nordman, Daniel J. (2019) <doi:10.1080/00031305.2019.1585288>.
Meinshausen, Nicolai (2006)
<http://www.jmlr.org/papers/volume7/meinshausen06a/meinshausen06a.pdf>.
Romano, Yaniv and Patterson, Evan and Candes, Emmanuel (2019)
<arXiv:1905.03222>. Tung, Nguyen Thanh and Huang, Joshua Zhexue and
Nguyen, Thuy Thi and Khan, Imran (2014) <doi:10.13140/2.1.2500.8002>.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
